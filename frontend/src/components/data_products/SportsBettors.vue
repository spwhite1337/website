<template>
  <div class="container">
    <hr>
    <p>Sports Bettors</p>
    <div class="container">
      <b-form-select v-model="league" :options="leagues" size="sm" class="mt-3"></b-form-select>
      <b-form-select v-model="random_effect" :options="random_effects" size="sm" class="mt-3"></b-form-select>
      <b-form-select v-model="condition" :options="conditions" size="sm" class="mt-3"></b-form-select>
    </div>
    <br>
    <input v-model="random_effect_value" type="text">
    <br><br>
    <button @click="sportsBettors">Bet on Sports</button>
    <p>Output from Sports Bettors: {{ sb_output }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SportsBettors',
  data () {
    return {
      leagues: ['College Football', 'NFL'],
      league: '',
      random_effects: ['team', 'opponent'],
      random_effect: 'team',
      random_effect_value: '',
      conditions: ['RushOnly', 'PassOnly', 'Offense', 'PointsScored', 'All'],
      condition: '',
      sb_output: ''
    }
  },
  methods: {
    sportsBettors () {
      const path = `http://localhost:5000/api/sportsbettors`
      axios.get(path, {
        params: {
          random_effect: this.random_effect,
          inputs: {
            RandomEffect: this.random_effect_value
          }
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
