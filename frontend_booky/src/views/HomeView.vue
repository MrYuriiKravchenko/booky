<template>
<div>
  <div class="home">
    <div id="app" class="main-content">
      <div class="slider-container">
        <Slider />
      </div>
    </div>
  </div>

  <section class="section">
    <div class="container">
      <div class="columns is-multiline">
      

        <div class="column is-12 has-text-centered">
          <a href="#" class="button is-link is-size-3 mt-6 mb-6">Кликните для начала</a>
        </div>
      </div>
    </div>
  </section>
</div>
</template>

<script>
import Slider from '@/components/Slider.vue';

export default {
  name: 'HomeView',
  components: {
    Slider
  },
};
</script>

<style lang="scss">
@import '~bulma'; 

.main-content {
  padding-top: 1rem;
}

.slider-container {
  margin-top: 2rem;
}
</style>
