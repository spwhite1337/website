<template>
<div>
    <h1>Work in Progress: Shield Your Eyes</h1>
    <h2>Label-Free Microfluidic Biosensors with Printed, Floating-Gate Transistors by Scott P. White</h2>
    <hr>
    <b>Overview:</b> The poorly kept secret of doctorate degrees is the work rarely matters as much as the experience
    and relationships you make during the process. The challenge of "Becoming an expert in something, no matter how
    niche" has formative characteristics on the student and instills in them a kind of humility and respect for detail
    that is hard to find outside the insulated academic environment.
    <br><br>
    There is some truth to the trope, "Academia is not 'real' life" and that truth is by design. The Academy is often a
    major part of the community it exists in but is always a contingent aspect not foundational. The work of
    colleges and universities can rarely justify itself, but rather exists to serve the system that begets it. Examples
    abound but include the development of citizenry through a liberal arts education, the training of people for work
    outside of academia, and the critique of the cultures it stems from. Now that I have been in the private sector a
    few years I understand that my Ph.D. project would have (maybe should have) been discarded after a few weeks of
    investment. But this "real-life" experience in the private sector is fraught with shortcomings -> namely a
    profound lack of introspection by those who are too detached from the "fake life" of academy.
    <br><br>
    <captioned-image
            :image="getImgUrl('gore_annex.jpg')" alt="Gore Annex"
            caption="The Chemical Engineering Building at the UMN, 'The Gore Annex'"
            position="right" size="30%">
    </captioned-image>
    Anecdotes abound from my career, but the laughable references to "the private sector" or the "free market" in
    industry are thrown around in situations as absurd as multi-trillion dollar international investment banks. People
    actually believe they operate within "freedom" constraints that differ from those of government institutions with
    webs of red-tape and bureaucracy. Not only are they seen as different from republic institutions, but they are
    implicitly assumed to be better by the lines of upper-management. In case my framing isn't clear, there is no
    functional difference between core institutions of Capital and those of the State. They are two sides of the same
    coin that operates in a hierarchical structure primarily motivated by its own self-preservation and external
    perception. The higher-ups in the private sector would do well to integrate themselves in Academia more and
    force themselves to see their work as contingent and accidental rather than the heroic endeavor they usually
    imagine.
    <br><br>
    The institutional character of Academia both depends on and influences the experiences of individual students.
    As stereotypes predict, the personalities of academics are especially eccentric - interactions with these folks is
    the real treat of the Ph.D. experience. Academics often give you fascinating insight into a
    sub-set of intellectual society. While most-but-definitely-not-all of the members of a Ph.D. organization are
    generally intelligent, they all very much value intelligence and intellectual pursuits and don't question its
    adoption as a guiding beacon for living life.
    <br><br>
    <b>Project Context:</b> Further elaboration on Academia is topic for another post, but the it is important to
    understand the defining characteristics of academic life as I outline the inspiration my specific Ph.D. project.
    It began an undergraduate seeking a career path. I was a good Chemical Engineering student that had experienced
    the process engineering industry through an internship with Monsanto in Muscatine, IA.
    <br><br>
    <b>Proof of Concept:</b>
    <captioned-image
          :image="getImgUrl('poc_figure.gif')" alt="POC Sketch"
          caption="Proof of Concept sketch of the Sensor Platform"
          position="right" size="30%">
    </captioned-image>
    <br><br>
    <b>Mechanistic Study:</b>
    <br><br>
    <b>Technology Development:</b>
  </div>
</template>
<script>
import CaptionedImage from '@/components/utils/CaptionedImage.vue'

export default {
    name: 'PhD',
    components: { 'captioned-image': CaptionedImage },
    methods: { getImgUrl (pic) { return require('@/assets/blog_posts/science/PhD/' + pic) } },
}
</script>