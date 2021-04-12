const app = Vue.createApp({});

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
  }
}

app.component('cards',  {
    data() {
      return {
        cardIndex: 0,
        front: true,
        correctCount: 0,
        courseDone: false,
      }
    },
    props: {
        cards: Array,
    },
    methods: {
      answer(correct){
        if (correct) {
          this.correctCount+=1;
        }
        if (this.cardIndex < this.cards.length - 1) {
          this.cardIndex+=1;
          this.front = true;
        } else {
          this.showScore();
        }
      },
      showScore(){
        this.courseDone = true;
        window.confetti.start(5000);
      },
      reset(){
        shuffleArray(this.cards);
        this.cardIndex = 0;
        this.correctCount = 0;
        this.front = true;
        this.courseDone = false;
        window.confetti.stop();
      }
    },
    computed: {
      card(){
        return this.cards[this.cardIndex];
      }
    },
    template: `
    <div class="columns is-centered">
      <div class="column is-half">
        <div 
          @click="front=!front" 
          class="card-box box is-flex is-align-items-center is-justify-content-center"
        >
          <h2 class="title">
            <span v-if="courseDone">{{ correctCount }}/{{ cards.length }} correct</span>
            <span v-else-if="front">{{ card.term }}</span>
            <span v-else>{{ card.definition }}</span>
          </h2>
        </div>

        <div class="buttons is-centered">
          <button :disabled="courseDone" @click="answer(true)" class="button is-success">
          ✔️
          </button>
          <button :disabled="courseDone" @click="answer(false)" class="button is-danger">
          X
          </button>
          <button v-if="courseDone" @click="reset" class=button is-primary>
          🔀
          </button>
        </div>
      </div>
    </div>
    `,
});
  
app.mount('#cards-vue');