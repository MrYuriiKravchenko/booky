<template>
  <div class="search-bar">
    <input 
      v-model="query" 
      @input="onInput" 
      @keyup.enter="onSearch"
      placeholder="Поиск..." 
      class="input" 
      type="text" 
    />
    <button @click="onSearch" class="button is-success">Поиск</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: '',
    };
  },
  methods: {
    onInput() {
      if (this.query.length === 0) {
        console.log('Input cleared.'); // Логирование очистки ввода
      }
    },
    onSearch() {
      console.log(`Search triggered with query: ${this.query}`);

      if (this.query.length > 2) {  // Минимальная длина запроса для поиска
        this.$router.push({ name: 'SearchResults', params: { query: this.query } });
        this.query = '';
        console.log('Search form cleared');
      } else {
        console.log('Query too short');
      }
    }
  }
};
</script>

<style>
.search-bar {
  position: relative;
  margin: 20px;
  display: flex;
  align-items: center;
}

.search-bar .input {
  width: 250px;
  margin-right: 10px;
}

.search-bar .button {
  margin-left: 10px;
}
</style>
поиск