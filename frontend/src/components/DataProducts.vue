<template>
  <div>
    <br>
      <p>
      Data Products use data to generate actionable insights. Peruse the following:
          <ul>
            <li><b>Magic Card Classifier:</b> Buzzfeed style app to determine the mana class of an input image</li>
            <li><b>Sports Betting Aid:</b> Bayesian Model that yields data-driven winning probabilities</li>
            <li><b>Presidents Speeches Search Engine:</b> Quick language classifier that connects search queries to a
            U.S. President and their official speeches</li>
          </ul>
      </p>
      <hr>
    <!--  Product Selector  -->
    <b-dropdown text="Data Products">
        <b-dropdown-item v-for="product in Products" :key="product.name" :value="product.name">
            <router-link :to="{ name: product.name }">{{ product.title }}</router-link>
        </b-dropdown-item>
    </b-dropdown>
    <transition name="slide-fade">
        <router-view></router-view>
    </transition>
  </div>
</template>

<script>
import DataProducts from '@/components/data_products'

export default {
  data () {
    return {
        Products: DataProducts
    }
  },
}
</script>

<style>
  /* Enter and leave animations can use different */
/* durations and timing functions.              */
.slide-fade-enter-active {
  transition: all .3s ease;
}
.slide-fade-leave-active {
  transition: all .3s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
</style>
