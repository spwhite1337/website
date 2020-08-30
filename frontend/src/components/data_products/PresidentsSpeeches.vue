<template>
  <div class="container">
    <hr>
      <div>
          <h3>Presidents Speeches Search</h3>
          <p>
              The decorum and norms of the United States Government have changed drastically during my lifetime thanks in
              large part to comedian-in-chief Donald Trump.
              The Miller Center provides a collection of presidents speeches given in their official capacity and I had an
              interest in searching through these speeches by topics.
              <br><br>
              The ability to search through a collection of text is great example of Natural Language Processing or NLP.
              This quick project takes this (small) corpus of presidents speeches and maps an input phrase to the
              president who it best matches and the specific speech it best matches.
              <br><br>
              Inputs should be short, descriptive phrases like, "Fake News" or "Vietnam Communists". If you put garbage
              queries in you will likely get spurious results. Future iterations will correct for this, but now this is all
              you get.
              <br><br>
              The code and results can be found
              <a href="https://github.com/spwhite1337/presidents-speeches" target="_blank">here</a>.
          </p>
      </div>
     <captioned-image
              :image="getImgUrl('best_words.jpg')" alt="Best" caption="Peak articulation"
              position="center" size="25%">
      </captioned-image>
      <hr>
      <div>
          <button @click="presidentsSpeeches">Search Presidents</button>
          <input v-model="query" type="text">
      </div>
      <div class="container" v-if="results.presidents">
           Best matched Presidents
          <ul v-for="president in results.presidents" :key="president">
            <li>{{ president.toUpperCase() }}</li>
          </ul>
          Most Similar Speeches:
          <ul v-for="(speech, idx) in results.speeches" :key="speech">
            <li><a :href="speech">Speech {{ idx + 1 }}</a></li>
          </ul>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
const path = process.env.VUE_APP_ROOT_API.concat('/api/presidentsspeeches')
import CaptionedImage from '@/components/utils/CaptionedImage.vue'

export default {
  name: 'PresidentsSpeeches',
  components: { 'captioned-image': CaptionedImage },
  data () {
    return {
      query: '',
      results: {}
    }
  },
  methods: {
    presidentsSpeeches () {
      axios.get(path, {
        params: {
          query: this.query
        }
      })
        .then(response => {
          this.results = response.data
        })
        .catch(error => {
          console.log(error)
        })
      return {}
    },
    getImgUrl (pic) {
        return require('@/assets/data_products/presidents_speeches/' + pic)
    }
  }
}
</script>
