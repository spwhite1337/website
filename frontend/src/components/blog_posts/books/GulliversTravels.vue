<template>
<div>
    <h1>Draft Post (Shield your eyes)</h1>
     <br>
    <h2>Gulliver's Travels, by Jonathan Swift</h2>
    <hr>
     Jonathan Swift, the author of Gulliver's Travels, is a wild man and former dean of St. Patrick's Cathedral in
       Dublin, Ireland. A member of the <a href="https://en.wikipedia.org/wiki/Scriblerus_Club"
   target="_blank">Scriblerus Club </a>, he presented Gulliver's Travels as a satirical work that is mocking the
       fashionable philosophies of his time - those that we often call "The Enlightenment". He explores different
       notions of "reason" and their effect on societal organizations in a form of "comparative government".
       <br><br>
       I plan to voyage through the book in the same order as Gulliver's (the protagonist) stops and highlight (i)
       the idea Swift is satirizing, (ii) any contemporary examples of such idea, and (iii) the "pre-modern" or
       "ancient" counterargument. In many cases, this aligns with Christian notions of reason, purpose, and politics
       that derive from Greek thinkers.
       <br><br>
       <b>Lilliput:</b> Gulliver is a trained surgeon who takes to sea after his patronage runs out. He finds himself
       shipwrecked and captured by a diminutive race of people - proportional humans shrunk to ~6 inches in height.
       They use Gulliver as a weapon against their long-term foes. His captivity is relieved when he shows mercy to
       officers who disobediently attacked him - something quite offensive to Lilliputian courts as they hold their
       culture and customs in high regards despite their ridiculousness (e.g. public officials almost literally
       jump through hoops to get appointed, people write diagonally). Their burial rituals coincide with their
       religion's eschatology - namely the eventual turning of the world (which they believe to be flat) upside down
       requiring the dead to be buried vertically, head-first. (As an interesting side note, Jonathan Swift was
       buried standing up in case of flooding).
        <br>
        <img :src="getImgUrl('lilliput.jpg')" alt="Lilliput" width="25%">
       <br><br>
       The high societal crime of Lilliput is lying and, conversely, the principal value is trust. Deceit and false
       accusations in court (Bearing False Witness to One's Neighbor, if you will) are high crimes with severe
       punishments. But, as Gulliver finds, the desecration of courts and civil monuments is also grave and he is
       sentenced to first death then blinding for urinating on the inflamed capital building. He eventually flees
       and takes a boat back to England.
       <br><br>
       <b>Analysis:</b> Lilliput is a great example of how arbitrary many cultural practices are. From the festivals to
       the resolution of conflicts in court - Swift satirizes these in a period of Imperial dominance from European
       colonizers. "You're not as cool as you think you are" but more eloquent.
       <br><br>
       <b>Brobdingnag:</b> The large people put him on display.
       <br><br>
       <b>Analysis:</b>
       <br><br>
       <b>Laputa to Japan:</b> Someone here makes people lick dirt and routinely executes them with poison dirt.
       <br><br>
       <b>Land of the Houyhnhnms:</b> Perfect reason in comparison to yahoos (humans that use reason to indulge
       themselves).
       <br><br>
       <b>Analysis:</b>
       <br><br>
  </div>
</template>

<script>
  export default {
    name: 'GulliversTravels',
    methods: { getImgUrl (pic) { return require('@/assets/blog_posts/books/GulliversTravels/' + pic) } }
  }
</script>