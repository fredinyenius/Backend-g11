import express from "express";
import cors from "cors";
import { usuarioRouter } from "./routes/usuario.routers.js";
import dotenv from "dotenv";

dotenv.config();


const servidor = express();
const PORT = 3000;

servidor.use(cors());
servidor.use(express.json());
servidor.use(usuarioRouter);

servidor.listen(PORT, () => {
    console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});