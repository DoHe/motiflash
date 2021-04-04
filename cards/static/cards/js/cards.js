const app = Vue.createApp({});

app.component('cards',  {
    data() {
      return {
        counter: 5,
      }
    },
    props: {
        cards: Array,
        title: String,
    },
    template: `
        Title: {{ title }}
        Cards: {{ cards }}
        Counter: {{ counter }}
    `,
});
  
app.mount('#cards-vue')