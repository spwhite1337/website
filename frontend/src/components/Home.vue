<template>
  <div class="container">
    <br>
    <h1>Scott P. White, Ph.D.</h1>
    <h3><em>The Most Modest Person of All Time</em></h3>
    <p>
      <br>
      <captioned-image
              :image="getImgUrl('headshot.png')" alt="Headshot" caption="Me in 2023"
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
      current employer. Of late, my time at AES has been dedicated to improving the product delivered by our utilities businesses.
      <br>
      <captioned-image
              :image="getImgUrl('indy.jpg')" alt="Indy" caption="Indy White, the Yorkie Terror"
              position="right" size="20%">
      </captioned-image>
      <br>
      With most of my keyboard-time spent behind a company firewall, I don't have much opportunity to display my 
      work and skills publicly. My best attempts are on disply on my Github and the Data Products section of this
      website contains (or will contain...) the productionalize version of the best ones. For now, the gambling 
      assisant I am working on is in the prototype stage but I am working to put it in production as fast as I can while maintaining full employment and keeping my newborn daughter alive. 
      <br><br>
      The Blog is all over the place and not intended to be a professional display - just personal enjoyment. 
      It is best described as a collection of drafted thoughts inspired by things I've read. <em>The 
	      Definition of Science</em> is probably my favorite but they are all similar quality.
      <br><br>
      Outside of the professional sphere, I am a husband to Brittany, father to Lucy, and a dog-keeper to 
      Indy the Yorkie Terror. Ideologically I'm a tortured combination of Catholic and Liberal with the 
      worst parts of each one contradictorily mixed together. Though the "Catholic" part should be mixed 
      with "American" and integrated beyond an ideology to a Way of Life but I'm too liberal to make any 
      coherent sense of it. I also subscribe to the ideology that doesn't like to put labels on anything 
      but I think that just means I'm a Millennial.
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
