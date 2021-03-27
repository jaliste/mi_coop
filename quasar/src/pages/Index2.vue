<template>
  <q-page-container>
    <q-page padding>
      <page-header>Quiero ser socio</page-header>
      <page-text>

  <div class="q-pa-md">
    <q-stepper
      v-model="step"
      ref="stepper"
      color="primary"
      animated
    >
      <q-step
        :name="1"
        title="Datos Personales"
        icon="settings"
        :done="step > 1"
      >
	<BlitzForm :schema="schema" v-model="formData"/>
      </q-step>

      <q-step
        :name="2"
        title="Create an ad group"
        caption="Optional"
        icon="create_new_folder"
        :done="step > 2"
      >
        An ad group contains one or more ads which target a shared set of keywords.
      </q-step>

      <q-step
        :name="3"
        title="Ad template"
        icon="assignment"
        disable
      >
        This step won't show up because it is disabled.
      </q-step>

      <q-step
        :name="4"
        title="Create an ad"
        icon="add_comment"
      >
        Try out different ad text to see what brings in the most customers, and learn how to
        enhance your ads using features like ad extensions. If you run into any problems with
        your ads, find out how to tell if they're running and how to resolve approval issues.
      </q-step>

      <template v-slot:navigation>
        <q-stepper-navigation>
          <q-btn @click="$refs.stepper.next()" color="primary" :label="step === 4 ? 'Finish' : 'Continue'" />
          <q-btn v-if="step > 1" flat color="primary" @click="$refs.stepper.previous()" label="Back" class="q-ml-sm" />
        </q-stepper-navigation>
      </template>
    </q-stepper>
  </div>

      </page-text>
    </q-page>
  </q-page-container>
</template>

<script>
import { BlitzForm } from "blitzar";

const schema = [
  { id: 'firstName' , label: 'First Name', component: 'input' },
  { id: 'lastName'  , label: 'Last Name',  component: 'input' },
  { id: 'nationalId', label: 'RUT',        component: 'input' },
  { id: 'birthDate' , label: 'Birth Date', component: 'input' },
  { id: 'civilStatus', label: 'Civil Status', component: 'input' },
  { id: 'nationality', label: 'Nationality', component: 'input' },
  { id: 'gender',     label: 'Gender', component: 'input' },
  { id: 'email',      label: 'Email', component: 'input' },
  { id: 'email_confirm', label: 'Confirm email', component: 'input' },

];

export default {
  name: "Apply",
  components: { BlitzForm },
  data () {
    return {
      schema: schema,
      step: 1
    }
  }
};
</script>

<style lang="css" scoped></style>
