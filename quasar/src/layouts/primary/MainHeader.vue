<template>
  <q-header>
    <q-toolbar>
      <q-btn
        id="toggleLeftDrawer"
        flat
        dense
        round
        @click="toggleLeftDrawer"
        aria-label="Menu"
      >
        <q-icon name="menu" />
      </q-btn>

      <q-toolbar-title>Huellas Verdes</q-toolbar-title>

      <span class="lang">
        <emoji
          :native="false"
          height="100%"
          :sheetSize="64"
          :emoji="lang.emoji"
          :size="28"
        />
      </span>
      <q-select dark dense color="white" v-model="lang" :options="langs" />

      <!-- <q-btn
        id="login"
        :ripple="false"
        color="white"
        text-color="primary"
        label="Login"
        v-if="!$store.getters['gqljwt/isAuthenticated']"
        no-caps
        @click="$router.push('/login-gql')"
      />
      <q-btn
        id="logout"
        :ripple="false"
        color="white"
        text-color="primary"
        label="Logout"
        v-if="$store.getters['gqljwt/isAuthenticated']"
        no-caps
        @click="logout"
      /> -->
      <q-btn
        id="apply"
        :ripple="false"
        color="white"
        text-color="primary"
        label="Become a member"
        no-caps
      />
      <q-btn
        id="login"
        :ripple="false"
        color="white"
        text-color="primary"
        label="Login"
        v-if="!$store.getters.isAuthenticated"
        no-caps
        @click="$router.push('/login')"
      />
      <q-btn
        id="logout"
        :ripple="false"
        color="white"
        text-color="primary"
        label="Logout"
        v-if="$store.getters.isAuthenticated"
        no-caps
        @click="logout"
      />
    </q-toolbar>
  </q-header>
</template>

<script>
export default {
  data() {
    return {
      showing: false,
      lang: {
        label: "Castellano",
        value: "es-cl",
        emoji: ":flag-cl:",
      },
      langs: [
        {
          label: "English",
          value: "en-us",
          emoji: ":flag-us:",
        },
        {
          label: "Castellano",
          value: "es-cl",
          emoji: ":flag-cl:",
        },
      ],
    };
  },
  methods: {
    setLang(lang) {
      this.lang = lang;
    },
    logout() {
      this.$store.dispatch("AUTH_LOGOUT").then(() => this.$router.push("/"));
      this.$router.go();
    },
    toggleLeftDrawer() {
      this.$store.commit("toggleLeftDrawer");
    },
  },
  created() {
    this.$i18n.locale = "en-us";
  },
  watch: {
    lang(lang) {
      this.$i18n.locale = lang.value;
      // import(`quasar/i18n/${lang}`).then(language => {
      //   this.$q.lang.set(language.default)
      // })
    },
  },
};
</script>

<style scoped>
.lang {
  margin-right: 15px;
  cursor: pointer;
  height: 28px;
}
.q-select {
  margin-right: 20px;
}
</style>
