<script setup>
// import { ref, onMounted } from "vue"
// import axios from "axios"

// const candidateFiles = ref([])

// onMounted(async () => {
//   try {
//     const response = await axios.get("http://127.0.0.1:8000/api/candidates")
//     candidateFiles.value = response.data.results
//     console.log(candidateFiles.value);
//   } catch (error) {
//     console.error("Error fetching data:", error)
//   }
// })
</script>

<template>
  <!-- <div>
    <h1>Candidate Files</h1>
    <ul>
      <li v-for="file in candidateFiles" :key="file?.id">
        <strong>{{ file?.file_path || "No path" }}</strong>
        ({{ file?.language || "Unknown" }})
        <pre>{{file.code}}</pre>
      </li>
    </ul>
  </div> -->
  <router-view/>
</template>
