<template>
  <div>
    <div class="about">
      <div class="hero is-link">
        <div class="hero-body has-text-centered">
          <h1 class="title">О нас</h1>
        </div>
      </div>
    </div>
    
    <section class="section">
      <nav class="breadcrumb" aria-label="breadcrumbs">
        <ul>
            <li><router-link to="/"><i class="fas fa-home" style="margin-right: 8px;"></i> Домашняя</router-link></li>
            <li class="is-active"><router-link to="/about" aria-current="true">О нас</router-link></li>
        </ul>
      </nav>
      <h1>Python разработчик</h1>
      <h3>Кравченко Юрий Александрович</h3>
      <span>Телефон: +79595331347</span>
    </section>
  </div>
</template>

<script>
export default {
  mounted() {
    document.title = 'О нас | Booky'
  }
}
</script>