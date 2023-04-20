import { Router } from "express";
import * as controllers from "../controllers/productos.controllers.js";
import { validarToken, esAdmin } from "../utils/wachiman.js";
export const productosRouter = Router();

productosRouter.post("/productos", validarToken, esAdmin, controllers.crearProducto);
