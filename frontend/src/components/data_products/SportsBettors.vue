<template>
  <div class="container">
    <hr>
    <p>Sports Bettors</p>
    <div class="container">
      <b-form-select v-model="league" :options="leagues" size="sm" class="mt-3"></b-form-select>
      <b-form-select v-model="random_effect" :options="random_effects" size="sm" class="mt-3"></b-form-select>
      <b-form-select v-model="feature_set" :options="feature_sets" size="sm" class="mt-3"></b-form-select>
    </div>
    <br>
    <input v-model="feature_vals.RandomEffect" type="text">
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

      // Set values of model
      feature_vals: {
        'RandomEffect': ''
      },

      sb_output: ''
    }
  },
  computed: {
    features: function () {
      if (this.condition === 'RushOnly') {
        return ['RushingYards', 'RushingAttempts']
      } else if (this.condition === 'PassOnly') {
        return ['PassingYards', 'PassingAttempts']
      } else if (this.condition === 'Offense') {
        return ['PassingYards', 'RushingYards', 'RushingAttempts', 'PassingAttempts']
      } else if (this.condition === 'PointsScored') {
        return ['TotalPoints']
      } else if (this.condition === 'All') {
        return ['All']
      } else {
        return []
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
          inputs: this.feature_vals
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
