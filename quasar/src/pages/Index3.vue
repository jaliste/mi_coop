<template>
  <div class="row justify-center full-width q-pa-md">
    <q-stepper
      v-model="step"
      ref="stepper"
      color="primary"
      animated
    >
      <q-step
        :name="1"
        title="Select campaign settings"
        icon="settings"
        :done="step > 1"
      >
        <div class="row justify-evenly q-gutter-sm">
          <BlitzForm :schema="schema" v-model="formData"/>
        </div>
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
</template>
<script>
  import { BlitzForm } from "blitzar";
  const today = new Date();
  const schema = [
  {
    id: "name",
    span: 1,
    component: "input",
    label: "Superhero name",
    subLabel: "Think of something cool.",
    required: true,
  },
  {
    id: "powerOrigin",
    span: 1,
    // SimpleOptionGroup is a simple wrapper I wrote for the HTML5 input with type radio, so it can be used easily with multiple options.
    component: SimpleOptionGroup,
    type: "radio",
    label: "Power origin",
    subLabel: "Where does your power come from?",
    options: [
      { label: "Mutation", value: "mutation" },
      { label: "Self taught", value: "self" },
      { label: "By item", value: "item" },
    ],
  },
  {
    id: "stamina",
    span: 2,
    component: "input",
    type: "range",
    label: "Stamina",
    parseInput: Number,
    defaultValue: 50,
    min: 0,
    max: 100,
  },
  {
    id: "power",
    span: 1,
    component: "input",
    label: "Power",
    subLabel:
      "Fill in a number. (this will get formatted as a number in the formData)",
    parseInput: Number,
    type: "number",
  },
  {
    id: "roleModel",
    span: 1,
    component: "select",
    label: "Role model",
    subLabel: "Who do you look up to?",
    slot: [
      { component: "option", value: "", slot: "" },
      {
        component: "option",
        value: "captain-america",
        slot: "Steve Rogers/Captain America",
      },
      { component: "option", value: "iron-man", slot: "Tony Stark/Iron Man" },
      { component: "option", value: "thor-odinson", slot: "Thor Odinson" },
      { component: "option", value: "the-hulk", slot: "Bruce Banner/The Hulk" },
      {
        component: "option",
        value: "black-widow",
        slot: "Natasha Romanoff/Black Widow",
      },
      { component: "option", value: "hawkeye", slot: "Clint Barton/Hawkeye" },
      {
        component: "option",
        value: "quicksilver",
        slot: "Pietro Maximoff/Quicksilver",
      },
      {
        component: "option",
        value: "scarlet-witch",
        slot: "Wanda Maximoff/Scarlet Witch",
      },
      { component: "option", value: "the-vision", slot: "The Vision" },
      {
        component: "option",
        value: "war-machine",
        slot: "James Rhodes/War Machine",
      },
      { component: "option", value: "falcon", slot: "Sam Wilson/Falcon" },
      {
        component: "option",
        value: "the-winter-soldier",
        slot: "Bucky Barnes/The Winter Soldier",
      },
      {
        component: "option",
        value: "black-panther",
        slot: "T'Challa/Black Panther",
      },
      {
        component: "option",
        value: "doctor-strange",
        slot: "Stephen Strange/Doctor Strange",
      },
      {
        component: "option",
        value: "spider-man",
        slot: "Peter Parker/Spider-Man",
      },
      {
        component: "option",
        value: "ant-man",
        slot: "Scott Lang/Ant-Man (Giant-Man)",
      },
      { component: "option", value: "wasp", slot: "Hope van Dyne/Wasp" },
      {
        component: "option",
        value: "captain-marvel",
        slot: "Carol Danvers/Captain Marvel",
      },
      {
        component: "option",
        value: "star-lord",
        slot: "Peter Quill/Star-Lord",
      },
      { component: "option", value: "gamora", slot: "Gamora" },
      {
        component: "option",
        value: "drax-the-destroyer",
        slot: "Drax the Destroyer",
      },
      {
        component: "option",
        value: "rocket-raccoon",
        slot: "Rocket (Raccoon)",
      },
      { component: "option", value: "groot", slot: "(Baby, Teenage) Groot" },
      { component: "option", value: "mantis", slot: "Mantis" },
      {
        component: "option",
        value: "daredevil",
        slot: "Matthew Murdock/Daredevil",
      },
      {
        component: "option",
        value: "jessica-jones",
        slot: "Jessica Jones (Jewel)",
      },
      {
        component: "option",
        value: "luke-cage",
        slot: "Carl Lucas/Luke Cage (Power Man)",
      },
      { component: "option", value: "iron-fist", slot: "Danny Rand/Iron Fist" },
      {
        component: "option",
        value: "the-punisher",
        slot: "Frank Castle/The Punisher",
      },
    ],
  },
  {
    id: "powerUps",
    span: 1,
    // SimpleOptionGroup is a simple wrapper I wrote for the HTML5 input with type checkbox, so it can be used easily with multiple options.
    component: SimpleOptionGroup,
    type: "checkbox",
    label: "Choose some power-ups",
    defaultValue: () => [],
    options: [
      {
        label: "ISO-8 Chrystal",
        value: "iso-8",
      },
      {
        label: "Health potion",
        value: "hp-potion",
      },
      {
        label: "Energy drink",
        value: "energy-potion",
      },
    ],
  },
  { span: 1 },
  {
    id: "consent",
    component: "input",
    type: "checkbox",
    span: 1,
    label: "Do you agree with our terms?",
    rules: [(val) => val || "You must accept our terms"],
    defaultValue: false,
  },
  {
    id: "submissionDate",
    span: 1,
    component: "input",
    type: "date",
    label: "Date of submission",
  },
];

export default {
  name: "PageIndex",
  components: { BlitzForm },
  data() {
    return {
      schema: schema,
      selectedDate: "",
      minWidth: 100,
      maxDays: 7,
      monthFormatter: this.monthFormatterFunc(),
      dayFormatter: this.dayFormatterFunc(),
      weekdayFormatter: this.weekdayFormatterFunc(),
      txt_colors: {
        base: "white",
        palta: "white",
        fruta: "white",
        huevos: "black",
      },
      colors: {
        base: "primary",
        palta: "green",
        fruta: "red",
        huevos: "amber ligthen-1",
      },
      resources: [
        {
          name: "John",
          events: {
            "2021-02-03": [
              {
                chip: "base",
                qty: 1,
                price: 5800,
              },
              {
                chip: "huevos",
                qty: 4,
                price: 1100,
              },
              {
                chip: "fruta",
                qty: 1,
                price: 1100,
              },
            ],
            "2021-02-17": [
              {
                chip: "base",
                qty: 1,
                price: 5800,
              },
              {
                chip: "huevos",
                qty: 2,
                price: 1100,
              },
              {
                chip: "palta",
                qty: 3,
                price: 1100,
              },
            ],
          },
        },
      ],
      resources2: [
        { id: 1, name: "Conference Room A" },
        { id: 2, name: "Hola" },
      ],
      bookings: [
        {
          id: 1,
          resource: 1,
          start: today.setHours(8, 0, 0, 0) / 1000,
          end: today.setHours(10, 0, 0, 0) / 1000,
        },
        {
          id: 2,
          resource: 1,
          start: today.setHours(11, 0, 0, 0) / 1000,
          end: today.setHours(12, 0, 0, 0) / 1000,
        },
        {
          id: 3,
          resource: 1,
          start: today.setHours(13, 0, 0, 0) / 1000,
          end: today.setHours(17, 0, 0, 0) / 1000,
        },
      ],
      bookingID: 10,
    };
  },
  methods: {
    handleCreate: function (booking) {
      // Give booking a unique ID and append to array.
      booking.id = ++this.bookingID;
      this.bookings.push(booking);
    },
    handleUpdate: function (booking) {
      // Find index of updated booking.
      const index = this.bookings.findIndex(function (stored) {
        return stored.id === booking.id;
      });

      this.bookings.splice(index, 1, booking);
    },
    handleDelete: function (booking) {
      // Find index of deleted booking.
      const index = this.bookings.findIndex(function (stored) {
        return stored.id === booking.id;
      });

      // Remove booking from array.
      this.bookings.splice(index, 1);
    },
    getHeadDay(timestamp) {
      return `${timestamp.date}`;
    },
    monthFormatterFunc() {
      const longOptions = { timeZone: "UTC", month: "long" };
      const shortOptions = { timeZone: "UTC", month: "short" };

      return QCalendar.createNativeLocaleFormatter(this.locale, (_tms, short) =>
        short ? shortOptions : longOptions
      );
    },

    weekdayFormatterFunc() {
      const longOptions = { timeZone: "UTC", weekday: "long" };
      const shortOptions = { timeZone: "UTC", weekday: "short" };

      return QCalendar.createNativeLocaleFormatter(this.locale, (_tms, short) =>
        short ? shortOptions : longOptions
      );
    },

    dayFormatterFunc() {
      const longOptions = { timeZone: "UTC", day: "2-digit" };
      const shortOptions = { timeZone: "UTC", day: "numeric" };

      return QCalendar.createNativeLocaleFormatter(this.locale, (_tms, short) =>
        short ? shortOptions : longOptions
      );
    },
  },
};
</script>
