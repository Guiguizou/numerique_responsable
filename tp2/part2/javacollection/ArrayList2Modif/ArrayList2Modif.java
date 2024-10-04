
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

import java.util.ArrayList;
import java.util.Iterator;

public class ArrayList2Modif {
    
    public static void main(String args[]) {
        ArrayList<String> list = new ArrayList<String>();
        insertElements(list, 1000000);
        accessElements(list);
        removeElements(list, 500000);
        accessElements(list);
    }


    public static void insertElements(ArrayList<String> list, int count) {
        for (int i = 0; i < count; i++) {
            list.add("Number is " + i);
        }
    }


    public static void accessElements(ArrayList<String> list) {
        Iterator<String> itr = list.iterator();
        while (itr.hasNext()) {
            itr.next();
        }
    }


    public static void removeElements(ArrayList<String> list, int count) {
        for (int i = 0; i < count; i++) {
            list.remove(0);
        }
    }
}

