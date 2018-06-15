<template>
  <div class="container">
     <button type="button" class="btn btn-primary">{{ msg }}</button>
   </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Food',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:8765/food/';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
