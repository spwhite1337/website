<template>
  <div class="container">
    <hr>
    <p>Sports Bettors</p>
    <div class="container">
      <b-form-select v-model="league" :options="leagues" size="sm" class="mt-3"></b-form-select>
      <b-form-select v-model="random_effect" :options="random_effects" size="sm" class="mt-3"></b-form-select>
      <b-form-select v-model="feature_set" :options="feature_sets" size="sm" class="mt-3"></b-form-select>
    </div>
    <div v-for="feature in inputs" :key="feature.name">
      <p>{{ feature.name }}</p>
      <input type="text" v-model="feature.value">
    </div>
    <br><br>
    <button @click="sportsBettors">Bet on Sports</button>
    <p>Output from Sports Bettors: {{ sb_output }}</p>
    <br>
    <div class="container" height="100%" width="100%">
<!--      <iframe :src="dashboard" frameborder="0"></iframe>-->
      <iframe :src="dashboard"
              scrolling="0"
              onload='javascript:(function(o){o.style.height=o.contentWindow.document.body.scrollHeight+"px";}(this));'
              style="height:3000px;width:100%;border:none;overflow:hidden;">
      </iframe>

    </div>

  </div>
</template>

<script>
import axios from 'axios'
const path = process.env.VUE_APP_ROOT_API.concat('/api/sportsbettors')
const dashpath = process.env.VUE_APP_ROOT_API.concat('/api/dash/sportsbettors')

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

      // Output
      sb_output: '',

      // Dashboard
      dashboard: dashpath
    }
  },
  computed: {
    inputs: function () {
      if (['College Football', 'NFL'].includes(this.league)) {
        if (this.feature_set === 'RushOnly') {
          return [
            {name: 'RandomEffect', value: ''},
            {name: 'Rushing Yards', value: ''},
            {name: 'Rushing Attempts', value: ''}
          ]
        } else if (this.feature_set === 'PassOnly') {
          return [
            {name: 'RandomEffect', value: ''},
            {name: 'Passing Yards', value: ''},
            {name: 'Passing Attempts', value: ''}
          ]
        } else if (this.feature_set === 'Offense') {
          return [
            {name: 'RandomEffect', value: ''},
            {name: 'Rushing Yards', value: ''},
            {name: 'Rushing Attempts', value: ''},
            {name: 'Passing Yards', value: ''},
            {name: 'Passing Attempts', value: ''}
          ]
        } else if (this.feature_set === 'PointsScored') {
          return [
            {name: 'RandomEffect', value: ''},
            {name: 'Total Points', value: ''}
          ]
        } else if (this.feature_set === 'All') {
          return [
            {name: 'RandomEffect', value: ''},
            {name: 'Home? (1=yes)', value: ''},
            {name: 'Rushing Yards (Adv)', value: ''},
            {name: 'Passing Yards (Adv)', value: ''},
            {name: 'Penalty Yards (Adv)', value: ''},
            {name: 'Possession Time (Adv, min)', value: ''},
            {name: 'Turnover Margin', value: ''},
            {name: 'First Downs (adv)', value: ''}
          ]
        } else {
          return []
        }
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
