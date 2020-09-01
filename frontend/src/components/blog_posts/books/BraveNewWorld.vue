<template>

<div>
    <h2>Draft Post, Shield your eyes</h2>
    <h2>Brave New World, by Aldous Huxley</h2>
    <hr>
     Rationally optimizing society. An endeavor that only makes sense in the abstract world of politics and theoretical
       societal structures, but fails at the level of a contradictory human. Brave New World is a dystopian novel that
       takes seriously the progressive arguments of techno-futurists in the early 20th century and takes them to their
       horrifying conclusions.
    <br>
    <captioned-image
        :image="getImgUrl('soma.jpg')" alt="Soma"
        caption="Soma, the most prescient part of the work."
        position="right" size="30%">
    </captioned-image>
    <br>
  </div>
</template>

<script>
import CaptionedImage from '@/components/utils/CaptionedImage.vue'
export default {
    name: 'BraveNewWorld',
    components: { 'captioned-image': CaptionedImage },
    methods: { getImgUrl (pic) { return require('@/assets/blog_posts/books/BraveNewWorld/' + pic) } }
}
</script>
