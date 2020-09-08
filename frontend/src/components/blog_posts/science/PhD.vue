<template>
<div>
    <h2><b>Label-Free Microfluidic Biosensors with Printed, Floating-Gate Transistors</b> by Scott P. White</h2>
    <hr>
    <b>Overview: </b>
    <br><br>
    <b>Proof of Concept:</b>
    <br><br>
    <b>Mechanistic Study:</b>
    <br><br>
    <b>Technology Development:</b>
  </div>
</template>
<script>
import CaptionedImage from '@/components/utils/CaptionedImage.vue'

export default {
    name: 'PhD',
    components: { 'captioned-image': CaptionedImage },
    methods: { getImgUrl (pic) { return require('@/assets/blog_posts/science/PhD/' + pic) } },
}
</script>