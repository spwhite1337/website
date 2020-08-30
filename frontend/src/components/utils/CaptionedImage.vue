<template>
<div :style="style">
    <figure>
        <img :src="image" :alt="alt">
        <figcaption>{{ caption }}</figcaption>
    </figure>
</div>
</template>
<script>
export default {
    name: 'captioned-image',
    props: ["image", "alt", "caption", "position", "size"],
    computed: {
        style () {
            return 'float: ' + this.position + ';' + ' width: ' + this.size + ';' + ' margin: 10px';
        }
    }
}
</script>
<style scoped>
figure {
    padding: 15px;
    width: 100%;
    box-shadow: 1px 2px 2px 1px lightgray;
    background-color: white
}
img {
    width: 100%;
    border: 1px solid lightgray
}
figcaption {
    font-style: italic
}
</style>

