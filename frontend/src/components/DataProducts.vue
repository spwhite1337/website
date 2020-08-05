<template>
  <div>
    <!--  Product Selector  -->
    <b-dropdown text="Data Products">
        <b-dropdown-item v-for="product in Products" :key="product.name" :value="product.name">
            <router-link :to="{ name: product.name }">{{ product.title }}</router-link>
        </b-dropdown-item>
    </b-dropdown>
    <router-view></router-view>
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