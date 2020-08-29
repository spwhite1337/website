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
figure {
    float: right;
    padding: 15px;
    width: 25%;
    box-shadow: 1px 2px 2px 1px lightgray
}
img {
    width: 100%;
    border: 1px solid lightgray
}
figcaption {
    font-style: italic
}
</style>

