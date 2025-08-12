<template>
    <div class="container">
        <br>
        <h3>You can contact me and / or get more information via many routes:</h3>
        <br>
        <ul>
            <li><button><a @click="showResume">Download Resume (Currently Out-of-Date)</a></button></li>
        </ul>
        <ul>
            <li>Email (Preferred): spwhite1337@gmail.com</li>
            <li><a href="https://www.linkedin.com/in/scott-p-white/" target="_blank">LinkedIn</a></li>
            <li><a href="https://github.com/spwhite1337" target="_blank">GitHub</a></li>
            <li>TikToks from 2019:
                <a href="https://www.tiktok.com/@scottdollabillz" target="_blank">ScottDollaBillz</a>
            </li>
        </ul>
    </div>
</template>
<script>
import Resume from '@/assets/Contact/ScottWhite_Resume.pdf'

export default {
    name: 'Contact',
    methods: { showResume () { window.open(Resume) } },
}
</script>
