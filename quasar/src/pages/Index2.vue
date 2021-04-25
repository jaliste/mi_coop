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
	      <BlitzForm :schema="schemaPersonalData" v-model="formData"/>
      </q-step>

      <q-step
        :name="2"
        title="Tu Membresía"
        caption="Optional"
        icon="create_new_folder"
        :done="step > 2"
      >
        <BlitzForm :schema="schemaMembership" v-model="formData"/>
      </q-step>

      <q-step
        :name="3"
        title="Arma tu canasta"
        icon="assignment"
      >
      <BlitzForm :schema="schemaArmaTuCanasta" v-model="formData"/>
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
import { BlitzForm, BlitzListForm } from "blitzar";

import {QInput, QOptionGroup, QSelect, QBtn} from 'quasar'
import Vue from 'vue'

Vue.component('QInput', QInput)
Vue.component('QOptionGroup', QOptionGroup)
Vue.component('QBtn',QBtn)
Vue.component('QSelect',QSelect)

const schemaPersonalData = [
  { id: 'firstName' , label: 'Nombres', component: 'QInput' },
  { id: 'lastName'  , label: 'Apellidos',  component: 'QInput' },
  { id: 'email',      label: 'Email', component: 'QInput', type:'email' },
  { id: 'email_confirm', label: 'Confirma tu email', component: 'QInput', type:'email'},
  { id: 'nationalId', label: 'RUT',        component: 'QInput' },
  { id: 'gender',     label: 'Género', component: 'QInput' },
  { id: 'birthDate' , label: 'Fecha de Nacimiento', component: 'QInput', type:'date' },
  { 
    id: 'civilStatus',
    label: 'Estado Civil',
    component: 'QOptionGroup',
    type: 'radio',
    options: [
      { label: 'Soltera(o)', value: 'soltero' },
      { label: 'Casada(o)', value: 'casado' },
      { label: 'Viudo(o)', value: 'viudo' },
      { label: 'Otro', value: 'item' },
    ],
  },
  { id: 'nationality', label: 'Nacionalidad', component: 'QInput' },
  { id: 'occupation', label: 'Ocupación/profesión', component: 'QInput'}
];

const schemaMembership = [

];

const fichas = [
  'Paltas',
]

const schemaArmaTuCanasta = [
  { 
    id: 'fichas',
    label: 'Fichas',
    subLabel: 'Elige las fichas para complementar tu canasta base' ,
    component: BlitzListForm,
    schema: [
      {
        component: 'QBtn',
        slot: '-',
        events: {
          click: (e, {deleteRow}) => deleteRow(),
        },
        outline: '',
        rounded: '',
        evaluatedProps: ['disabled'],
        disabled: (val, {rowIndex, formData}) => rowIndex === formData.length,
        componentClasses: 'outline rounded',
        span: '20px',
      },
      { 
        id: 'cantidad',
        label: 'Cantidad',
        component: 'QInput', 
        parseInput: Number,
        type: 'number',
        "input-class": 'text-right',
      },
      { 
        id: 'producto',
        label: 'Ficha',
        component: 'QSelect',
        options: [
          { 
            label: 'Paltas',
            precioPorFicha: 1650,
            descrip: '',
          },
          {
            label: "Huevos",
            precioPorFicha: 1100,
            descrip: '',
          },
          {
            label: "Frutas",
            precioPorFicha: 1100,
            descrip: '',
          } 
        ]
      },
      { 
        id: 'precio_ficha',
        label: 'Valor por Ficha', component: 'QInput',
        readonly:'',
      },
      { id: 'total',
        label: 'Valor',
        component: 'QInput',
        readonly: '',
      }       
    ],
  }
];

export default {
  name: "Apply",
  components: { BlitzForm },
  data () {
    return {
      schemaPersonalData: schemaPersonalData,
      schemaMembership: schemaMembership,
      schemaArmaTuCanasta: schemaArmaTuCanasta,
      step: 1
    }
  }
};
</script>

<style lang="css" scoped></style>
