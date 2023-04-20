import express from "express";
import cors from "cors";
import { usuarioRouter } from "./routes/usuario.routers.js";
import { productosRouter } from "./routes/productos.routes.js";
import dotenv from "dotenv";

dotenv.config();
console.log()


const servidor = express();
const PORT = 3000;

servidor.use(cors());
servidor.use(express.json());
servidor.use(usuarioRouter);
servidor.use(productosRouter);

servidor.listen(PORT, () => {
    console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});