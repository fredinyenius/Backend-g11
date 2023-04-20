import { Router } from "express";
import * as controllers from "../controllers/productos.controllers.js";

export const productosRouter = Router();

productosRouter.post("/productos", controllers.crearProducto);
