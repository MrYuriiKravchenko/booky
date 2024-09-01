<template>
    <nav class="navbar is-link" role="navigation" aria-label="main navigation" style="min-height: 5rem;">
        <div class="navbar-brand">
            <router-link class="navbar-item is-size-4" to="/">RateMyReads</router-link>
        </div>

        <div id="navbar-menu" class="navbar-menu">
            <div class="navbar-start">
                <router-link to='/' class="navbar-item">Домашняя</router-link>
                <router-link to='/about' class="navbar-item">О нас</router-link>
                <router-link to="/books" class="navbar-item">Книги</router-link>
            </div>

            <div class="navbar-end">
                <div class="navbar-item">
                    <div class="buttons">
                        <template v-if="$store.state.user.isAuthenticated">
                            <router-link to="/dashboard/my-account" class="button is-info">Мой аккаунт</router-link>
                        </template>

                        <template v-else>
                            <router-link to="/sign-up" class="button is-primary"><strong>Регистрация</strong></router-link>
                            <router-link to="/log-in" class="button is-light">Войти</router-link>
                        </template>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>