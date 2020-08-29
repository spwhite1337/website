<template>
    <div class="container">
        <img :src="image" alt="alt" width="25%">
        <p>{{ caption }}</p>
    </div>
</template>
<script>
export default {
    name: 'captioned-image',
    props: ["image", "alt", "caption"]
}
</script>

