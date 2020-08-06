<template>
  <div>
    <p>Blog Posts</p>

      <b-dropdown text="Books">
          <b-dropdown-item v-for="post in books" :key="post.name" :value="post.name">
            <router-link :to="{ name: post.name }">{{ post.title }} by {{ post.author }}</router-link>
          </b-dropdown-item>
      </b-dropdown>

      <b-dropdown text="Science">
          <b-dropdown-item v-for="post in science" :key="post.name" :value="post.name">
            <router-link :to="{ name: post.name }">{{ post.title }}</router-link>
          </b-dropdown-item>
      </b-dropdown>

      <b-dropdown text="Political">
          <b-dropdown-item v-for="post in political" :key="post.name" :value="post.name">
            <router-link :to="{ name: post.name }">{{ post.title }}</router-link>
          </b-dropdown-item>
      </b-dropdown>

      <transition name="slide-fade">
          <router-view></router-view>
      </transition>
  </div>
</template>

<script>
import BlogPosts from '@/components/blog_posts'

export default {
data () {
  return {
        books: BlogPosts.Books,
        political: BlogPosts.Political,
        science: BlogPosts.Science
    }
}}
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