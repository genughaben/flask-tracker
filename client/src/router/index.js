import Vue from 'vue';
import Router from 'vue-router';
import HelloWorld from '@/components/HelloWorld';
import Food from '@/components/Food';
import Entry from '@/components/Entry';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld,
    },
    {
      path: '/food',
      name: 'Food',
      component: Food,
    },
    {
      path: '/entry',
      name: 'Entry',
      component: Entry,
    },
  ],
});
