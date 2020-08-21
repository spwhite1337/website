<template>
<div>
    <h2>Job Search Post-Academia</h2>
    <hr>
     Academic science is a strange place. It is an institution comprised of rational, intelligent people all pursuing a
    predominantly passion-driven and irrational endeavor: getting a Ph.D. This peculiarity is amplified in the field I
    stem from, Chemical Engineering, because a bachelor's degree is far more employable than most other degrees
    including a Chemical Engineering Ph.D. Sure, the job roles and benefits differ, but the key barrier of 'employable
    or not' is readily surmounted after a bachelor's but increased if a Ph.D. is pursued in ChemE.
     <br><br>
    <img :src="getImgUrl('brick_in_the_wall.jpg')" alt="Brick in the Wall" width="25%">
    <br>
     One could protest, 'A degree is not job training, the purpose of going to university is to become a better
    person/citizen/Christian (in the old days)!' to which I respond, 'lol, I graduated high school right at the
    recession I needed to get that paper.' While it's true that that was my mentality during most of undergrad, I still
    went on to get my Ph.D. when I had two informal offers from industry near bachelor's graduation. Those offers would
    haunt my dreams on multiple occasions during graduate school.
     <br><br>
     Towards the end of my Ph.D. I had to outline the next move I would make in order to keep food on the table. The
    process is highlighted in the following figure and best interpreted as four pursuits: (i) Naive Chemical Engineering
    Pursuit, (ii) Serious Chemical Engineering Pursuit, (iii) Data Science
    Pursuit, (iv) Data Science Pursuit Post-Insight.
     <br><br>
        <em>Insert Figure Here</em>
     <br><br>
     The timeline of the graph is elaborated as:<br>
     <ul>
       <li>
         Fall 2016: Naively applied to jobs on the University Website (mostly). "How hard can this be? I have a good
           degree from a top 5 institution with a well-known advisor and respectable publication record."
       </li>
       <li>
         Winter 2016/Spring 2017: While I didn't get any hits to start, I figured I would pursue a possible career as
           a Start-Up entrepreneur promoting the technology developed during my Ph.D. "You miss 100% of the shots you
           don't take", as Michael Scott once said.
       </li>
       <li>
         Summer 2017: Parallel goals. Applied for Chemical Engineering jobs more seriously and also pursued the
           Start-Up through an <a href="https://www.nsf.gov/news/special_reports/i-corps/" target = "_blank">I-Corps
           program</a>.
       </li>
       <li>
         Fall 2017: Start-Up started looking very difficult, seriously applied to Chemical Engineering jobs. I
           landed my first on-site interview with Micron (got denied).
       </li>
       <li>
         Winter/Spring 2018: Defended my Ph.D. and pursued the Start-Up full-time as a post-doc.
       </li>
       <li>
         Summer 2018: Quit the Start-Up. Vacationed as Brittany's trophy boyfriend for a bit while raising the pup.
           Eventually developed the resume skills for Data Science and started applying vigorously.
       </li>
       <li>
         Fall 2018: Participated in an <a href="https://www.insightdatascience.com/" target = "_blank">Insight Data
           Science Fellowship Program</a> that led to three offers. I accepted the one for Strong Analytics.
       </li>
        <li>
         Fall 2019: Applied for 3 jobs, got on-site interviews for 2 of them (Corteva and AES), got the offer for AES
            but denied for Corteva.
      </li>
     </ul>
     <br>
     In summary, the process is confusing, demoralizing, dehumanizing, ego-killing, self-confidence-killing, and
    frustrating. I understand why people stay in academia (as the skills directly transfer) but I had to get out.
    If you're in a similar position I have a few pieces of advice/wisdom: (i) applying online gets you a 10% callback
    rate at best, (ii) using distant contacts for job networking is part of the norms and not awkward - you should
    do it, (iii) use a recruiter and abuse them, (iv) be willing to relocate as geographical restrictions are the
    biggest turn-off to employers, (v) lower your standards until you get experience, (vi) take care of yourself
    during the job hunt.
  </div>
</template>

<script>
  export default {
    name: 'JobSearch',
    methods: { getImgUrl (pic) { return require('@/assets/blog_posts/political/JobSearch/' + pic) } },
  }
</script>
