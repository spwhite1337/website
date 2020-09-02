<template>

<div>
    <h2>Draft Post, Shield your eyes</h2>
    <h2>Brave New World, by Aldous Huxley</h2>
    <hr>
     Rationally optimizing society. An endeavor that only makes sense in the abstract world of politics and theoretical
       societal structures, but fails at the level of a contradictory human. Brave New World is a dystopian novel that
       takes seriously the progressive arguments of techno-futurists in the early 20th century and takes them to their
       horrifying conclusions.
    <br><br>
        More interestingly, it is a novelizations of Nietzsche's ideas about <em>The Last Man</em> and his critiques of
    Liberal Capitalism and Enlightenment reason. Such a topic is beyond the scope of my capabilities but might get
    revisited in another post someday.
   <br><hr>
    <captioned-image
        :image="getImgUrl('soma.jpg')" alt="Soma"
        caption="Soma, the most prescient part of the work."
        position="right" size="30%">
    </captioned-image>
<b>Summary:</b> Set in the 26th Century, Europe had reached it goals of a scientific, progressive, and stable society.
    The World State cultivates its citizens into different castes that are conditioned to fully in a manner that is
    mutually beneficially for them and for society as a whole. They find immense joy out of consuming material goods,
    satiating their sexual appetites, and consuming soma - a psychoactive pharmaceutical that is generously distributed
    by the World State.
    <br><br>
    To enable their profound scientific progress in genetic engineering and psychology, the culture of the World
    State is one of Extreme individualism with a group identity engineered by caste: Alphas are the highest while
    gammas are the lowest. Ostensibly the system functions perfectly, but cracks form as seen through two alphas:
    Bernard and Helmholtz. Bernard is an alienated psychologist while Helmholtz is a bored writer.
    <br><br>
    Despite being an alpha, Bernard doesn't fit in well in the World State and suspect he was accidentally subjected to
    alcohol during his birth - resulting in him being a "small" alpha and inspiring insecurities. After causing some
    trouble he ventured to the outskirts of society and meets John, man who grew up outside the hyper-scientific
    individualism of the World State and instead developed among a psuedo-Native American tribe while learning
    english from the works of Shakespeare.
    <br><br>
    Bernard brings John back to the world state where he bonds with the bored and literary-minded Helmholtz. 
  </div>
</template>

<script>
import CaptionedImage from '@/components/utils/CaptionedImage.vue'
export default {
    name: 'BraveNewWorld',
    components: { 'captioned-image': CaptionedImage },
    methods: { getImgUrl (pic) { return require('@/assets/blog_posts/books/BraveNewWorld/' + pic) } }
}
</script>
