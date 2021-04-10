const app = Vue.createApp({});

app.component('cards',  {
    data() {
      return {
        cardIndex: 0,
        front: true,
      }
    },
    props: {
        cards: Array,
    },
    computed: {
      card(){
        return this.cards[this.cardIndex];
      }
    },
    template: `
    <div @click="front=!front" class="card">
      <div class="card-content">
        <div class="title">
          <span v-if="front">
            {{ card.term }}
          </span>
          <span v-else>
            {{ card.definition }}
          </span>
        </div>
      </div>
    </div>

    <div class="field is-grouped">
      <p class="control">
        <button :disabled="cardIndex <= 0" @click="cardIndex-=1" class="button">
          Previous
        </button>
      </p>
      <p class="control">
        <button :disabled="cardIndex >= cards.length - 1" @click="cardIndex+=1" class="button">
          Next
        </button>
      </p>
  </div>
    `,
});
  
app.mount('#cards-vue')