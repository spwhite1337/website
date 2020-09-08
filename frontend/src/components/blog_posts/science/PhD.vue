<template>
<div>
    <h1>Work in Progress: Shield Your Eyes</h1>
    <h2>Label-Free Microfluidic Biosensors with Printed, Floating-Gate Transistors by Scott P. White</h2>
    <hr>
    <b>Overview:</b> The secret of Ph.D.'s is that the work rarely matters as much as the experience and relationships
    you make during the process. The challenge of "Becoming an expert in something, no matter how niche" has formative
    characteristics on the student and instills in them a kind of humility and respect for detail that is hard to find
    outside the insulated academic environment. Now that I have been in the private sector a few years I understand that
    my Ph.D. project would have (maybe should have) been discarded after a few weeks of investment.
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