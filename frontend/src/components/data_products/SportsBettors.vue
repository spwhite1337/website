<template>
  <div class="container">
    <hr>
    <p>Sports Bettors</p>
    <div class="container">
      <b-form-select v-model="league" :options="leagues" size="sm" class="mt-3"></b-form-select>
      <b-form-select v-model="random_effect" :options="random_effects" size="sm" class="mt-3"></b-form-select>
      <b-form-select v-model="feature_set" :options="feature_sets" size="sm" class="mt-3"></b-form-select>
    </div>
    <div v-for="feature in inputs">
      <li>{{ feature.name }}, {{ feature.value }}</li>
    </div>
    <br><br>
    <button @click="sportsBettors">Bet on Sports</button>
    <p>Output from Sports Bettors: {{ sb_output }}</p>
  </div>
</template>

<script>
import axios from 'axios'
const path = process.env.API_URL.concat('/sportsbettors')

export default {
  name: 'SportsBettors',
  data () {
    return {
      // Select League
      leagues: ['College Football', 'NFL'],
      league: '',
      // Configure Model
      random_effects: ['team', 'opponent'],
      random_effect: '',

      feature_sets: ['RushOnly', 'PassOnly', 'Offense', 'PointsScored', 'All'],
      feature_set: '',

      sb_output: ''
    }
  },
  computed: {
    inputs: function () {
      if (this.condition === 'RushOnly') {
        return [{name: 'RushingYards', value: ''}]
      } else if (this.condition === 'PassOnly') {
        return [{name: 'RushingYards', value: ''}]
      } else if (this.condition === 'Offense') {
        return [{name: 'RushingYards', value: ''}]
      } else if (this.condition === 'PointsScored') {
        return [{name: 'RushingYards', value: ''}]
      } else if (this.condition === 'All') {
        return {'all': ''}
      } else {
        return [{name: 'RushingYards', value: ''}]
      }
    }
  },
  methods: {
    sportsBettors () {
      axios.get(path, {
        params: {
          league: this.league,
          random_effect: this.random_effect,
          feature_set: this.feature_set,
          inputs: this.inputs
        }
      })
        .then(response => {
          this.sb_output = response.data.sb_output
        })
        .catch(error => {
          console.log(error)
        })
      return {}
    }
  }
}
</script>
