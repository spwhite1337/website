<template>
    <div class="container">
        <br>
        <h3>You can contact me and / or get more information via many routes:</h3>
        <br>
        <ul>
            <li><button><a @click="showResume">Download Resume (Updated Summer 2020)</a></button></li>
        </ul>
        <ul>
            <li>Email (Preferred): spwhite1337@gmail.com</li>
            <li><a href="https://www.youtube.com/user/spwhite1337" target="_blank">Youtube Channel for SPWhite1337</a></li>
            <li>Give me money on <a href="https://venmo.com/hubba" target="_blank">Venmo</a> if you like</li>
            <li><a href="https://twitter.com/ScottDollaBillz" target="_blank">Twitter</a> is my platform of choice</li>
            <li><a href="https://www.linkedin.com/in/scott-p-white/" target="_blank">LinkedIn</a></li>
            <li><a href="https://github.com/spwhite1337" target="_blank">GitHub</a></li>
            <li><a href="https://www.instagram.com/scottdollabills/" target="_blank">
                Instagram for one selfie a year</a>
            </li>
            <li>TikTok so I can rack up the likes:
                <a href="https://www.tiktok.com/@scottdollabillz" target="_blank">ScottDollaBillz</a>
            </li>
            <li>Snapchat for a Dog pic once a month: ScottDollaBillz</li>
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