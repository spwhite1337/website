<template>
  <div>
    <p>Data Products</p>

    <!--  Product Selector  -->
    <div class="container">
      <b-form-select v-model="data_product" :options="data_products" size="sm" class="mt-3"></b-form-select>
    </div>

    <!--   Sports Bettors   -->
    <div class="container" v-if="showSportsBettors"><SportsBettors/></div>

    <!--  Presidents Speeches  -->
    <div class="container" v-if="showPresidentsSpeeches"><PresidentsSpeeches/></div>

    <!--  Card Classifier  -->
    <div class="container" v-if="showCardClassifier"><CardClassifier/></div>

  </div>
</template>

<script>
import PresidentsSpeeches from './data_products/PresidentsSpeeches.vue'
import CardClassifier from './data_products/CardClassifier.vue'
import SportsBettors from './data_products/SportsBettors.vue'

export default {
  components: {
    PresidentsSpeeches,
    CardClassifier,
    SportsBettors
  },
  data () {
    return {
      data_products: ['Sports Bettors', 'Magic Card Classifier', 'Presidents Speeches'],
      data_product: ''
    }
  },
  computed: {
    showCardClassifier: function () {
      return this.data_product === 'Magic Card Classifier'
    },
    showSportsBettors: function () {
      return this.data_product === 'Sports Bettors'
    },
    showPresidentsSpeeches: function () {
      return this.data_product === 'Presidents Speeches'
    }
  },
  methods: {
  },
  created () {
  }
}
</script>
