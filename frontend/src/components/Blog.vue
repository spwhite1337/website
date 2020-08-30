<template>
  <div>
      <br>
      <p>
          My posts fall into three categories:
          <ul>
            <li><b>Books:</b> Reports and Essays summarizing and analysing big-brain books</li>
            <li><b>Science:</b> Essays related to my official profession</li>
            <li><b>Political:</b> Comments on problems in the terrestrial realm</li>
          </ul>
      </p>
      <hr>
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

      <div id="blog-post">
          <transition name="slide">
              <router-view></router-view>
          </transition>
          <hr>
          <p>
              User Login and Comments are coming soon!
          </p>
          <hr>
      </div>

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

<style scoped>
.enter { transform: translateX(100%) }
.enter-to { transform: translateX(0) }
.slide-enter-active { position: absolute }

.leave { transform: translateX(0) }
.leave-to { transform: translateX(-100%) }

.slide-enter-active,
.slide-leave-active { transition: all 100ms ease-in-out }

#blog-post {
    border: 1px solid lightgray;
    box-shadow: 1px 2px 2px 1px lightgray;
    margin: 2%;
    padding: 2%
}
</style>