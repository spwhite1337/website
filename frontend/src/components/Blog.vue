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

      <transition name="slide">
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
.enter { transform: translateX(100%) }
.enter-to { transform: translateX(0) }
.slide-enter-active { position: absolute }

.leave { transform: translateX(0) }
.leave-to { transform: translateX(-100%) }

.slide-enter-active,
.slide-leave-active { transition: all 100ms ease-in-out }
</style>