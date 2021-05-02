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
        progressColor: '',
        confetti: null,
      }
    },
    props: {
        cards: Array,
        courseId: String,
    },
    methods: {
      answer(correct){
        if (correct) {
          this.correctCount+=1;
          this.givePoints('card_correct');
        }
        if (this.cardIndex < this.cards.length - 1) {
          this.cardIndex+=1;
          this.front = true;
        } else {
          this.showScore();
        }
      },
      showScore(){
        if (this.correctCount / this.cards.length > 0.8) {
          if (this.correctCount == this.cards.length) {
            this.givePoints('course_perfect');
          } else {
            this.givePoints('course_finished');
          }
          this.progressColor = 'is-success';
          window.confetti({
            particleCount: 500,
            spread: 500,
          });
        } else {
          this.progressColor = 'is-danger';
          this.givePoints('course_finished');
        }
        this.courseDone = true;
      },
      reset(){
        shuffleArray(this.cards);
        this.cardIndex = 0;
        this.correctCount = 0;
        this.front = true;
        this.courseDone = false;
        this.progressColor = '';
        window.confetti.reset();
      },
      givePoints(reason){
        fetch(`/points?id=${this.courseId}&reason=${reason}`)
      }
    },
    computed: {
      card(){
        return this.cards[this.cardIndex];
      },
      progress(){
        if (this.courseDone) {
          return 1;
        }
        return this.cardIndex / this.cards.length;
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

        <div class="block">
          <progress class="progress" :class="progressColor" :value="progress" max="1">{{ value }}%</progress>
        </div>
      </div>
    </div>
    `,
});
  
app.mount('#cards-vue');