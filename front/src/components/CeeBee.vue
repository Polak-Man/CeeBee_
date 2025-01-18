<template>
  <form @submit.prevent="submitForm">
    <div class="container d-flex flex-column align-items-center justify-content-center vh-100">
      <div class="card">
        <div class="card-header">
          <h1 class="card-title">CeeBee</h1>
        </div>
        <div class="card-body">
          <input type="file" @change="handleFileUpload" accept="image/*,video/*" class="form-control" />
          <input type="text" v-model="textInput" placeholder="Saisissez votre texte ici" class="form-control" />
          <label>
            <input type="checkbox" v-model="showPseudo" />
            Afficher Pseudo ?
          </label>
          <div class="checkbox-list">
            <label v-for="name in names" :key="name">
              <input type="checkbox" :value="name" v-model="selectedNames" />
              {{ name }}
            </label>
          </div>
          <div class="duration-inputs">
            <input type="number" v-model="durationSec" placeholder="Durée en s" class="form-control" />
            <input type="number" v-model="durationMs" placeholder="en ms" class="form-control" />
          </div>
        </div>
        <input type="submit" name="Vlider" id="submit_form" />
      </div>
    </div>
  </form>
</template>

<script>
import axios from 'axios';
import '../assets/ceebee_style.css';

export default {
  data() {
    return {
      textInput: '',
      showPseudo: false,
      names: ['Aëlys', 'Alexis', 'Logan', 'Mattéo'],
      selectedNames: [],
      durationSec: null,
      durationMs: null,
      file: null,
    };
  },
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
      if (this.file) {
        console.log('Fichier uploadé:', this.file.name);
      }
    },
    async submitForm() {
      const formData = new FormData();
      formData.append('file', this.file);
      formData.append('textInput', this.textInput);
      formData.append('showPseudo', this.showPseudo);
      formData.append('selectedNames', JSON.stringify(this.selectedNames));
      formData.append('durationSec', this.durationSec);
      formData.append('durationMs', this.durationMs);

      try {
        const response = await axios.post('https://localhost:7030/api/CeeBee', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        console.log('Réponse de l\'API:', response.data);
      } catch (error) {
        console.error('Erreur lors de l\'envoi des données:', error);
      }
    },
  },
};
</script>

<style scoped>
/* Votre CSS ici */
</style>