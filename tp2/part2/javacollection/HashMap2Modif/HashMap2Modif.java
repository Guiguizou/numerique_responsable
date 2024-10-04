/*
 * Copyright (c) 2022, Adel Noureddine, Université de Pays et des Pays de l'Adour.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the
 * GNU General Public License v3.0 only (GPL-3.0-only)
 * which accompanies this distribution, and is available at
 * https://www.gnu.org/licenses/gpl-3.0.en.html
 *
 * Author : Adel Noureddine
 */

 import java.util.*;  

 public class HashMap2Modif {
     public static void main(String args[]) {
         HashMap<Integer, String> map = new HashMap<Integer, String>();
 
         insertElements(map, 1000000);
         accessElements(map);
         removeElements(map, 500000);
         accessElements(map);
     }
 
     public static void insertElements(HashMap<Integer, String> map, int count) {
         for (int i = 0; i < count; i++) {
             map.put(i, "Number is " + i);
         }
     }
 
     public static void accessElements(HashMap<Integer, String> map) {
         for (Map.Entry<Integer, String> m : map.entrySet()) {
             m.getKey();   
             m.getValue(); 
         }
     }
 
     public static void removeElements(HashMap<Integer, String> map, int count) {
         for (int i = 0; i < count; i++) {
             map.remove(i);
         }
     }
 }