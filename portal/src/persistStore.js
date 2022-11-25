import { createPinia } from "pinia";
const pinia = createPinia();

pinia.use((context) => {
  const storeId = context.store.$id;
  const serializer = {
    serialize: JSON.stringify,
    deSerealize: JSON.parse,
  };

  //trae cambios desde el local storage
  const fromStorage = serializer.deSerealize(
    window.localStorage.getItem(storeId)
  );

  if (fromStorage) {
    context.store.$patch(fromStorage);
  }
  //Escucha los cambios en el store y los actualiza
  context.store.$subscribe((mutation, state) => {
    window.localStorage.setItem(storeId, serializer.serialize(state));
  });
});

export { pinia };
