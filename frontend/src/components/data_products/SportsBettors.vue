<template>
  <div class="container">
    <hr>
    <h3>Sports Bettors</h3>
    <br>
    <p>
      The great state of Indiana has introduced me to the world of online sports betting and it is a real treat.
      I primarily use FanDuel to take advantage of combination bets including (i) which team will win, (ii) what
      the spread will be, and (iii) the over / under for total points in the game.
      <br><br>
      The dashboard below presents results from a bayesian regression on three responses: (i) the probability of the
      selected team winning against the select opponent, (ii) the probability the spread or margin of victory will be
      at least as high as presented, and (iii) the total number of points in the game. The results are specific to a
      model that control for different sets of inputs.
      <br><br>
      See the code and diagnostics of the various models on the repo:
      <a href="https://github.com/spwhite1337/sports-bettors" target="_blank">Repo</a>
    </p>
    <hr>
    <div class="container" id="dashboard">
      <iframe :src="dashboard" height="2000px" width="100%" style="border:0"></iframe>
    </div>
  </div>
</template>

<script>
const dashpath = process.env.VUE_APP_ROOT_API.concat('/api/dash/sportsbettors')

export default {
  name: 'SportsBettors',
  data () {
    return {
      // Dashboard
      dashboard: dashpath
    }
  },
}
</script>
<style scoped>
#dashboard {
  border: 1px solid lightgray;
  box-shadow: 1px 2px 2px 1px lightgray;
}
</style>