<template>
<div>
    <h1>Draft Post (Shield your eyes)</h1>
     <br>
    <h2>Gulliver's Travels, by Jonathan Swift</h2>
    <hr>
     Jonathan Swift, the author of Gulliver's Travels, is a wild man and former dean of St. Patrick's Cathedral in
       Dublin, Ireland. A member of the <a href="https://en.wikipedia.org/wiki/Scriblerus_Club"
       target="_blank">Scriblerus Club </a>, he presented Gulliver's Travels as a satirical work that is mocking the
       fashionable philosophies of his time - those that we often call "The Enlightenment" - while also critiquing
       European politics, religions, and wars. He explores different notions of "reason" and their effect on societal
       organizations in a form of "comparative government".
       <br><br>
        <captioned-image
          :image="getImgUrl('swift_grave.jpg')" alt="Swift's Grave" caption="Swift's Grave at St. Patrick's Cathedral
          in Dublin. He was buried standing up due to the tendency for the cathedral to flood (unclear how this helps)"
          position="right" size="30%">
        </captioned-image>
       <br>
        Pound for pound, the book is very rich. I will focus on two of the societies Gulliver travels too and outline
       the main lessons we can draw from Swift's analysis - the relationship between ancients / moderns and his
        criticism of Science.
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
        <br><br>
       The high societal crime of Lilliput is lying and, conversely, the principal value is trust. Deceit and false
       accusations in court (Bearing False Witness to One's Neighbor, if you will) are high crimes with severe
       punishments. But, as Gulliver finds, the desecration of courts and civil monuments is also grave and he is
       sentenced to first death then blinding for urinating on the inflamed capital building. He eventually flees
       and takes a boat back to England.
    <br>
    <captioned-image
            :image="getImgUrl('lilliput.jpg')" alt="Lilliput" caption="The Little Land of Lilliput"
            position="left" size="30%">
    </captioned-image>
    <br>
       <b>Analysis:</b> Lilliput is a great example of how arbitrary many cultural practices are. From the festivals to
       the resolution of conflicts in court - Swift satirizes these in a period of Imperial dominance from European
       colonizers. Despite some wise values, they also quarrel with neighboring tribes over trivial interpretations of
        legal texts, outline absurd requirements for government positions, and drastically overestimate their place in
        the universe.
    <br><br>
        Contextualizing the work aids in this interpretation. In the 17th and 18th century Europe was the dominant global
        power with England on the up-and-up. Recent inventions such as paper and the sextant enabled exploration and
        colonizations of lands of legend to ancient thinkers prompting widespread ideologies of chauvinism and
        European / Ethno superiority. Swift mocks this notion with fictional society filled with comparably
        arbitrariness as 18th century England.
    <br><br>
        More broadly, he attacks the "moderns" in the ancient vs. moderns debate that was popular amongst philosophical
        circles at the time. Many saw the ancients (e.g. Aristotle, Plato, St. Paul) as outdated and irrelevant as we
        had progressed beyond them on a path of enlightenment.
       <br><br>
       <b>Laputa:</b>
       <br><br>
       <b>Analysis:</b>
       <br><br>
  </div>
</template>

<script>
import CaptionedImage from '@/components/utils/CaptionedImage.vue'
export default {
    name: 'GulliversTravels',
    components: { 'captioned-image': CaptionedImage },
    methods: { getImgUrl (pic) { return require('@/assets/blog_posts/books/GulliversTravels/' + pic) } }
}
</script>