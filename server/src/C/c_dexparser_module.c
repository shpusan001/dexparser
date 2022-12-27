#include <stdlib.h>
#include <stdio.h>
#include <wchar.h>

typedef struct protoFull
{
    wchar_t *shorty;
    wchar_t *return_typ;
    wchar_t **parameter;
} ProtoFull;

wchar_t *convertTypeToNormal(wchar_t *type)
{
    switch (type[0])
    {
    case L'V':
        return L"void";
        break;
    case L'Z':
        return L"boolean";
        break;
    case L'B':
        return L"byte";
        break;
    case L'S':
        return L"short";
        break;
    case L'C':
        return L"char";
        break;
    case L'I':
        return L"int";
        break;
    case L'J':
        return L"long";
        break;
    case L'F':
        return L"float";
        break;

    case L'D':
        return L"double";
        break;

    case L'L':
        return type + 1;
        break;

    case L'[':
        return type;
        break;

    default:
        return type;
        break;
    }
}

wchar_t **getTypeListFull(wchar_t *path, int off, int *typeIds, wchar_t **stringFull)
{
    size_t pathSize = wcslen(path);

    char *cpath = malloc(sizeof(char) * (pathSize + 1));
    wcstombs(cpath, path, pathSize + 1);

    FILE *fp;
    fp = fopen(cpath, "r");

    int result = fseek(fp, off, SEEK_SET);

    int size;
    fread(&size, sizeof(int), 1, fp);

    short *typeListIds = malloc(sizeof(short) * size);
    wchar_t **typeListFull = malloc(sizeof(wchar_t *) * size);

    fread(typeListIds, sizeof(short), size, fp);

    for (int i = 0; i < size; i++)
    {
        int typeIdx = typeListIds[i];
        int stringIdx = typeIds[typeIdx];
        typeListFull[i] = convertTypeToNormal(stringFull[stringIdx]);
    }

    fclose(fp);
    return typeListFull;
}

wchar_t *getTypeListFullStr(wchar_t *path, int off, int *typeIds, wchar_t **stringFull)
{
    size_t pathSize = wcslen(path);

    char *cpath = malloc(sizeof(char) * (pathSize + 1));
    wcstombs(cpath, path, pathSize + 1);

    FILE *fp;
    fp = fopen(cpath, "r");

    int result = fseek(fp, off, SEEK_SET);

    int size;
    fread(&size, sizeof(int), 1, fp);

    short *typeListIds = malloc(sizeof(short) * size);
    wchar_t *output = malloc(sizeof(wchar_t) * 2560000000);

    fread(typeListIds, sizeof(short), size, fp);
    wcscat(output, L"[");
    for (int i = 0; i < size; i++)
    {
        int typeIdx = typeListIds[i];
        int stringIdx = typeIds[typeIdx];
        wcscat(output, L"\"");
        wcscat(output, convertTypeToNormal(stringFull[stringIdx]));
        wcscat(output, L"\",");
    }
    wcscat(output, L"]");
    fclose(fp);
    return output;
}

wchar_t **getTypeListFullEOF(wchar_t *path, int off, int *typeIds, wchar_t **stringFull)
{
    size_t pathSize = wcslen(path);

    char *cpath = malloc(sizeof(char) * (pathSize + 1));
    wcstombs(cpath, path, pathSize + 1);

    FILE *fp;
    fp = fopen(cpath, "r");

    int result = fseek(fp, off, SEEK_SET);

    int size;
    fread(&size, sizeof(int), 1, fp);

    short *typeListIds = malloc(sizeof(short) * size);
    wchar_t **typeListFull = malloc(sizeof(wchar_t *) * (size + 1));

    fread(typeListIds, sizeof(short), size, fp);

    for (int i = 0; i < size; i++)
    {
        int typeIdx = typeListIds[i];
        int stringIdx = typeIds[typeIdx];
        typeListFull[i] = convertTypeToNormal(stringFull[stringIdx]);
    }
    typeListFull[size] = (wchar_t *)EOF;

    fclose(fp);
    return typeListFull;
}

wchar_t *getProtoFull(wchar_t *path, int size, int off, int *typeIds, wchar_t **stringFull)
{
    // [
    //     {
    //         "shorty" : 함수이름 스트링 데이터 (str),
    //         "return_type" : 리턴타입 스트링 데이터 (str),
    //         "parameters" : [ 파라미터 타입에 대한 스트링 데이터(str), ... ]
    //     },
    //     ...
    // ]

    size_t pathSize = wcslen(path);

    char *cpath = malloc(sizeof(char) * (pathSize + 1));
    wcstombs(cpath, path, pathSize + 1);

    FILE *fp;
    fp = fopen(cpath, "r");

    fseek(fp, off, SEEK_SET);

    wchar_t *output = malloc(sizeof(wchar_t) * 2560000000);

    wcscat(output, L"[");

    for (int i = 0; i < size; i++)
    {
        wcscat(output, L"{");

        int shorty_idx, parameter_off, return_type_idx;

        fread(&shorty_idx, sizeof(int), 1, fp);
        fread(&return_type_idx, sizeof(int), 1, fp);
        fread(&parameter_off, sizeof(int), 1, fp);

        wcscat(output, L"\"shorty\":\"");

        const wchar_t *tmpShorty = stringFull[shorty_idx];
        wcscat(output, tmpShorty);

        wcscat(output, L"\",");

        wcscat(output, L"\"return_type\":\"");
        int stringIdx = typeIds[return_type_idx];
        const wchar_t *tmpRType = convertTypeToNormal(stringFull[stringIdx]);
        wcscat(output, tmpRType);
        wcscat(output, L"\",");

        if (parameter_off == 0)
        {
            wcscat(output, L"\"parameter\":[]");
        }
        else
        {
            wcscat(output, L"\"parameter\":[");
            wchar_t **parameters = getTypeListFullEOF(path, parameter_off, typeIds, stringFull);
            while (*parameters != (wchar_t *)EOF)
            {
                wcscat(output, L"\"");
                wcscat(output, *parameters);
                wcscat(output, L"\",");
                parameters = parameters + 1;
            }
            wcscat(output, L"]");
        }

        wcscat(output, L"},");
    }

    wcscat(output, L"]");

    return output;
}

// ProtoFull **getProtoFull(wchar_t *path, int size, int off, int *typeIds, wchar_t **stringFull)
// {
//     // [
//     //     {
//     //         "shorty" : 함수이름 스트링 데이터 (str),
//     //         "return_type" : 리턴타입 스트링 데이터 (str),
//     //         "parameters" : [ 파라미터 타입에 대한 스트링 데이터(str), ... ]
//     //     },
//     //     ...
//     // ]

//     size_t pathSize = wcslen(path);

//     char *cpath = malloc(sizeof(char) * (pathSize + 1));
//     wcstombs(cpath, path, pathSize + 1);

//     FILE *fp;
//     fp = fopen(cpath, "r");

//     int result = fseek(fp, off, SEEK_SET);

//     ProtoFull **protoFull = malloc(sizeof(ProtoFull *) * size);

//     for (int i = 0; i < size; i++)
//     {
//         ProtoFull *protoFullUnit = malloc(sizeof(ProtoFull));
//         int shorty_idx, parameter_off, return_type_idx;

//         fread(&shorty_idx, sizeof(int), 1, fp);
//         fread(&return_type_idx, sizeof(int), 1, fp);
//         fread(&parameter_off, sizeof(int), 1, fp);

//         printf("++++++1-1\n");
//         printf("%d\n", shorty_idx);
//         printf("%d\n", parameter_off);
//         printf("%d\n", return_type_idx);
//         printf("++++++1-2\n");

//         protoFullUnit->shorty = stringFull[shorty_idx];

//         int stringIdx = typeIds[return_type_idx];
//         protoFullUnit->return_typ = stringFull[stringIdx];

//         wprintf(protoFullUnit->shorty);
//         printf("\n");
//         wprintf(protoFullUnit->return_typ);
//         printf("\n");

//         if (parameter_off == 0)
//         {
//             protoFullUnit->parameter = NULL;
//         }
//         else
//         {
//             protoFullUnit->parameter = getTypeListFull(path, parameter_off, typeIds, stringFull);
//         }

//         // printf("+++++++++2-1\n");
//         // int length = sizeof(protoFullUnit->parameter) / sizeof(protoFullUnit->parameter[0]);
//         // for (int i = 0; i < length; i++)
//         // {
//         //     wprintf(protoFullUnit->parameter[i]);
//         //     printf("\n");
//         // }
//         // printf("+++++++++2-2\n");

//         protoFull[i] = protoFullUnit;

//         printf("+++++++++3\n");
//     }

//     printf("+++++++++4\n");
//     return protoFull;
// }