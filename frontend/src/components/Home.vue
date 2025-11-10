<template>
  <div class="container">
    <br>
    <h1>Scott P. White, Ph.D.</h1>
    <h3><em>The Most Modest Person of All Time</em></h3>
    <p>
      <br>
      <captioned-image
              :image="getImgUrl('headshot.png')" alt="Headshot" caption="Me in 2018"
              position="left" size="25%">
      </captioned-image>
      <br>
      I'm Scott White and welcome to my site. I hail from the great state of Iowa but have since done a
      Midwest tour to Minneapolis, Chicago, and Indianapolis.
      <br><br>
      I am an academy-certified Chemical Engineer with a BS from the University of Iowa and a PhD from The
      University of Minnesota. Beyond scholarship, I am a private-sector-certified Data Scientist having worked for
      <a href="https://www.strong.io/" target="_blank">Strong Analytics</a>, a consulting firm in Chicago, and
      <a href="http://aes.com/" target="_blank">AES</a>, an energy company with a heavy renewables portfolio and my
      current employer.
      <br>
      <captioned-image
              :image="getImgUrl('indy.jpg')" alt="Indy" caption="Indy White, the Yorkie Terror"
              position="right" size="20%">
      </captioned-image>
      <br>
      Far more importantly, I am a husband to Brittany, father to Lucy,  and a dog-keeper to Indy the Yorkie Terror.
      Ideologically I'm a tortured combination of Catholic and Liberal with the worst parts of each one
      contradictorily mixed together. Though the "Catholic" part should be mixed with "American" and integrated
      beyond an ideology to a Way of Life but I'm too liberal to make any coherent sense of it. I also subscribe to the
      ideology that doesn't like to put labels on anything but I think that just means I'm a Millennial.
      <br><br>
      Explore the Data Products section to see some examples of my skills in Data Analytics, the Sports Bettors app is
      my favorite.
      <br><br>
      The Blog is all over the place, but mostly serves as a repository of Book reviews for pretentious stuff I read.
      <em>The Definition of Science</em> is probably my favorite but they are all similar quality.
    </p>
  </div>
</template>

<script>
import CaptionedImage from '@/components/utils/CaptionedImage.vue'

export default {
    name: 'Home',
    components: { 'captioned-image': CaptionedImage },
    methods: { getImgUrl (pic) { return require('@/assets/Home/' + pic) } },
}
</script>
