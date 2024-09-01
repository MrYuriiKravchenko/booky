<template>
    <div class="courses">

        <div class="hero is-link">
            <div class="hero-body has-text-centered">
                <h1 class="title">{{ book.title }}</h1>
            </div>
        </div>


        <section class="section">
            <div class="container">
                <div class="columns content">
                    <div class="column is-2">
                        <div class="card">
                            <div class="card-image">
                                <figure class="image is-2by3">
                                    <img src="https://bulma.io/assets/images/placeholders/1280x960.png" alt="Placeholder image">
                                </figure>
                            </div>
                        </div>
                    </div>

                    <div class="column is-10">
                        <h3>{{ book.author }}</h3>
                        <hr class="is-divider">
                        {{ book.description }}
                        <hr class="is-divider">


                        <h4>Рейтинг книги</h4>
                        <div v-if="ratings.length > 0">
                            <div>
                                <span v-for="n in 5" :key="n" class="icon">
                                    <i class="fas" :class="n <= averageRating ? 'fa-star' : 'fa-star-o'"></i>
                                </span>
                                <span>{{ averageRating.toFixed(1) }}/5 на основе {{ ratings.length }} оценок</span>
                            </div>
                        </div>
                        <div v-else>
                            <p>Рейтинг отсутствует</p>
                        </div>
                        <hr class="is-divider">


                        <div v-if="isAuthenticated">
                            <h4>Оцените книгу</h4>
                            <div>
                                <span v-for="n in 5" :key="n" class="icon" @click="setUserRating(n)">
                                    <i class="fas" :class="n <= userRating ? 'fa-star' : 'fa-star-o'"></i>
                                </span>
                            </div>
                            <button class="button is-link" @click="submitRating">Отправить рейтинг</button>
                            <hr class="is-divider">
                        </div>
                        <div v-else>
                            <p class="has-text-danger is-size-4">Нужно авторизоваться, чтобы оценить книгу.</p>
                            <hr class="is-divider">
                        </div>

                        <h4>Дополнительная информация</h4>
                        <p>ISBN: {{ book.isbn }}</p>
                        <p>Дата публикации: {{ book.pub_date }}</p>
                        <p>Язык: {{ book.language }}</p>
                        <hr class="is-divider">
                        <h4>Жанры</h4>
                        <p v-if="book.genre && book.genre.length > 0">{{ book.genre.join(', ') }}</p>
                        <p v-else>Жанры не указаны</p>
                        <hr class="is-divider">

                        <h3>Рецензии</h3>
                        <div v-for="comment in comments" :key="comment.id" class="box">
                            <p>{{ comment.user }}</p>
                            <strong>{{ comment.title_text }}</strong>
                            <p>{{ comment.text }}</p>
                        </div>


                        <div class="notification is-danger" v-if="errorMessage">
                            <ul>
                                <li v-for="error in errorMessage.split(', ')" :key="error">{{ error }}</li>
                            </ul>
                        </div>

                        <div v-if="isAuthenticated">
                            <form v-on:submit.prevent="submitComment">
                                <div class="field">
                                    <label class="label">Введите ваше имя пользователя</label>
                                    <div class="control">
                                        <input type="text" class="input" v-model="comment.user" placeholder="Введите ваше имя пользователя" required>
                                    </div>
                                </div>

                                <div class="field">
                                    <label class="label">Заголовок</label>
                                    <div class="control">
                                        <input type="text" class="input" v-model="comment.title_text" required>
                                    </div>
                                </div>

                                <div class="field">
                                    <label class="label">Текст рецензии</label>
                                    <div class="control">
                                        <textarea class="textarea" v-model="comment.text" required></textarea>
                                    </div>
                                </div>

                                <div class="field">
                                    <div class="control">
                                        <button class="button is-link">Опубликовать</button>
                                    </div>
                                </div>
                            </form>
                        </div>
                        <div v-else>
                            <p class="has-text-danger is-size-4">Нужно авторизоваться, чтобы оставлять рецензии.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            book: {},
            comments: [],
            ratings: [],
            userRating: 0, 
            comment: {
                user: '',   
                title_text: '',
                text: ''
            },
            isAuthenticated: false,
            successMessage: '',  
            errorMessage: ''     
        };
    },
    computed: {
        averageRating() {
            if (this.ratings.length === 0) return 0;
            const total = this.ratings.reduce((sum, rating) => sum + rating.rating, 0);
            return total / this.ratings.length;
        }
    },
    methods: {
        getAuthHeaders() {
            return {
                Authorization: `Bearer ${localStorage.getItem('token')}`
            };
        },
        checkAuthentication() {
            this.isAuthenticated = !!localStorage.getItem('token');
        },
        fetchBookData() {
            const slug = this.$route.params.slug;
            axios.get(`books/${slug}/`)
                .then(response => {
                    this.book = response.data;
                })
                .catch(error => {
                    console.error("Error fetching book data:", error);
                });
        },
        fetchComments() {
            const slug = this.$route.params.slug;
            axios.get(`comments/${slug}/`)
                .then(response => {
                    this.comments = response.data;
                })
                .catch(error => {
                    console.error("Error fetching comments:", error);
                });
        },
        fetchRatings() {
            const slug = this.$route.params.slug;
            axios.get(`books/${slug}/ratings/`)
                .then(response => {
                    this.ratings = response.data;
                })
                .catch(error => {
                    console.error("Error fetching ratings:", error);
                });
        },
        setUserRating(rating) {
            this.userRating = rating;
        },
        submitRating() {
            const slug = this.$route.params.slug;
            const ratingData = {
                rating: this.userRating
            };

            axios.post(`books/${slug}/ratings/`, ratingData, { headers: this.getAuthHeaders() })
                .then(response => {
                    this.ratings.push(response.data);
                    this.userRating = 0; 
                    this.successMessage = "Ваш рейтинг был успешно отправлен!";
                    this.errorMessage = ''; 
                })
                .catch(error => {
                    if (error.response && error.response.data) {
                        this.errorMessage = `Ошибка: ${error.response.data.detail}`;
                    } else if (error.request) {
                        this.errorMessage = "Ответ от сервера не был получен.";
                    } else {
                        this.errorMessage = `Ошибка: ${error.message}`;
                    }
                    this.successMessage = ''; 
                });
        }
    },
    created() {
        this.checkAuthentication();  
        this.fetchBookData();
        this.fetchComments();
        this.fetchRatings();
    }
};
</script>
