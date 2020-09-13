<template>
<div>
    <h1>Work in Progress: Shield Your Eyes</h1>
    <h2>Label-Free Microfluidic Biosensors with Printed, Floating-Gate Transistors by Scott P. White</h2>
    <hr>
    <b>Overview:</b> The poorly kept secret of doctorate degrees is the work rarely matters as much as the experience
    and relationships you make during the process. The challenge of "Becoming an expert in something, no matter how
    niche" has formative characteristics on the student and instills in them a kind of humility and respect for detail
    that is hard to find outside the insulated academic environment. Now that I have been in the private sector a few
    years I understand that my Ph.D. project would have (maybe should have) been discarded after a few weeks of
    investment.
    <br><br>
    The people you interact with often give you a fascinating insight into a sub-set of intellectual society. While
    most-but-definitely-not-all of the members of a Ph.D. organization are generally intelligent, they all very much
    value intelligence and intellectual pursuits and don't question its adoption as a guiding beacon for living life.
    <captioned-image
          :image="getImgUrl('gore_annex.jpg')" alt="Gore Annex"
          caption="The Chemical Engineering Building at the UMN, 'The Gore Annex'"
          position="right" size="30%">
    </captioned-image>
    <br><br>
    <b>Proof of Concept:</b>
    <captioned-image
          :image="getImgUrl('poc_figure.gif')" alt="POC Sketch"
          caption="Proof of Concept sketch of the Sensor Platform"
          position="right" size="30%">
    </captioned-image>
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