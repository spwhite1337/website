<template>
  <div class="container">
    <img :src="getImgUrl('headshot.png')" alt="Headshot" width="25%">
    <p>
      I'm Scott White and welcome to my channel. I hail from the great state of Iowa but have since done a
      Midwest tour to Minneapolis, Chicago, and Indianapolis.
      <br><br>
      I am an academy-certified Chemical Engineer with a BS from the University of Iowa and a PhD from The
      University of Minnesota but I am a private-sector-certified Data Scientist having worked for a consulting firm in
      Chicago, (<a href="https://www.strong.io/" target="_blank">Strong Analytics</a>, and
      <a href="http://aes.com/" target="_blank">AES</a>, a energy company with a heavy renewable portfolio
      (my current employer).
      <br><br>
      Far more importantly, I am a fiance to Brittany Forkus and a dog-keeper to Indy the Yorkie Terror.
      Ideologically I'm a tortured combination of Catholic and Liberal with the worst parts of each one
      contradictorily mixed together. Though the "Catholic" part should be mixed with "American" and integrated
      beyond an ideology but I'm too liberal to make any coherent sense of it. I also subscribe to the ideology that
      doesn't like to put labels on anything but I think that just means I'm a Millennial.
      <img :src="getImgUrl('indy.JPG')" alt="Indy" width="25%">
      <br><br>
      Explore the Data Products section to see some examples of my skills in Data Analytics, the Sports Bettors app is
      my favorite.
      <br><br>
      The Blog is all over the place, but mostly serves as a repository of Book reviews for pretentious stuff I read.
    </p>
  </div>
</template>

<script>
export default {
    name: 'Home',
    methods: {
        getImgUrl (pic) {
                return require('@/assets/Home/' + pic)
            }
        },
    }
</script>