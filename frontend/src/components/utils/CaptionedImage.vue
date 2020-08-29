<template>
    <figure>
        <img :src="image" :alt="alt">
        <figcaption>{{ caption }}</figcaption>
    </figure>
</template>
<script>
export default {
    name: 'captioned-image',
    props: ["image", "alt", "caption"]
}
</script>
<style scoped>
img {
    width: 100%;
    border: 1px solid #000
}
figure {
    float: left;
    padding: 15px;
    width: 25%
}
figcaption {
    font-style: italic
}
</style>

